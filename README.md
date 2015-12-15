# GX-Toray-mRNA

1. Place process_toray_mRNA.py in your path
2. Create a folder with the individual toray files (NormalizedResults for each cell)
3. Create a target.txt file and place it in the same folder
4. Run process_toray_mRNA.py target.txt
5. Run the QC r script which will generate plots and a table in a folder QC/. This script is not executable, but will be
6. Run the knitr report generation, which expects three folders (Data/, QC/, TorayQC/)
