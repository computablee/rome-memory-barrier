#!/bin/sh

mv ../results/scale_results ..
mv ../results/uprof_results ..
rm -rf ../results

echo "********************Parsing Events CSVs***********************"
python3 events_parser.py

echo "********************Parsing Metrics CSVs**********************"
python3 metrics_parser.py

echo "*******************Verifying Parsed Data**********************"
python3 verify_parser.py

echo "****************Creating CSVs for Graphing********************"
python3 graph_parser.py

echo "*****************Creating CSVs for Tables*********************"
python3 table_parser.py

echo "***********Creating Scalability CSVs for Graphing*************"
python3 scale_parser.py

echo "***************Moving Results to Single Folder****************"
mkdir ../results
mv ../uprof_results* ../results
mv ../graph_data ../results
mv ../scale_results ../results
rm -rf ../fp_rate ../fp_speed ../int_rate ../int_speed
