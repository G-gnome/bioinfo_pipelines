#!/usr/bin/bash -l
#SBATCH -p short -c 12 --mem 24gb --out logs/LSU_extract.log

CPU=12
module load samtools
module load barrnap

for genome_file in $(ls genomes/*.fasta genomes/*.fna); do
    base=$(basename -- "$genome_file")
    base="${base%.*}"

    mkdir -p results/LSU/$base

    cat results/LSU/$base.SSEARCH.tab | while read QUERY TARGET PID X GAPO GAPE QS QE TS TE EVALUE SCORE; do
        samtools faidx $genome_file $TARGET
    done > results/LSU/$base/LSU_scaffolds.fasta

barrnap results/LSU/$base/LSU_scaffolds.fasta -o results/LSU/$base/rrna.fasta --kingdom euk

grep -A 1 "28S_rRNA" results/LSU/$base/rrna.fasta | awk '/28S_rRNA/{name=$0; getline; seq=$0; if(length(seq) > max_len) {max_len=length(seq); max_seq=name "\n" seq}} END{print max_seq}' > results/LSU/$base/LSU_seq.fasta

perl -i -p -e "s/>/>${base}_/" results/LSU/$base/LSU_seq.fasta

done
