# NEW

This repository provides a reference implementation of *NEW* as described in the paper:<br>
> NEW: A Generic Learning Model for Tie Strength Prediction in Networks.<br>
The *NEW* algorithm mainly focuses on the link prediction of undirected graph weighted network

The experimental partition data required by the paper is stored under the data directory, which may be slightly deviated based on the operation of different machines.If you want to repartition the test data, please refer to the following instructions to complete the test results.

### Basic Usage

#### Example
To run *NEW* on celegans network, execute the following command from the project home directory:<br/>
	``python code/main.py --input ../data/celegans.csv --cache True``

#### Options
You can check out the other options available to use with *node2vec* using:<br/>
	``python code/main.py --help``
  
#### Input
The supported input format is an netwrok data:
	
    node1_id node2_id weight
