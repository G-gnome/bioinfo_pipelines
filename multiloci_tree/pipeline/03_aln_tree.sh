#!/usr/bin/bash -l
#SBATCH -p short -c 16 -N 1 -n 1 --mem 24gb --out logs/tree.log

module load mafft
module load fasttree
module load clipkit
mkdir -p aln

# Alignment

for genome_file in $(ls genomes/*.fasta genomes/*.fna); do
    base=$(basename -- "$genome_file")
    base="${base%.*}"

    # ITS alignment
    cat results/ITSx/$base/ITSx.full.fasta > aln/${base}_ITS_full_LSU.fas

    # LSU alignment (excluding the first line)
    tail -n +2 results/LSU/$base/LSU_seq.fasta >> aln/${base}_ITS_full_LSU.fas

done

# Combine individual alignments into a single file
cat aln/*_ITS_full_LSU.fas > aln/ALL_ITS_full_LSU.fas

# Perform MAFFT alignment on the combined file
mafft aln/ALL_ITS_full_LSU.fas > aln/ALL_ITS_full_LSU.fasaln

# Combine alignments
clipkit aln/ALL_ITS_full_LSU.fasaln

# Tree build
FastTreeMP -nt -gamma aln/ALL_ITS_full_LSU.fasaln.clipkit > aln/Rhodotorula_ITS_LSU.fasaln.tre

