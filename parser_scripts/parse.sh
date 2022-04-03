#!/bin/sh

echo "********************Parsing Events CSVs***********************"
python3 events_parser.py

echo "********************Parsing Metrics CSVs**********************"
python3 metrics_parser.py

echo "*******************Verifying Parsed Data**********************"
python3 verify_parser.py

echo "**********Creating Events/Metrics CSVs for Graphing***********"
python3 graph_parser.py

echo "***********Creating Scalability CSVs for Graphing*************"
python3 scale_parser.py
