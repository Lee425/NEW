# NEW

This repository provides a reference implementation of *NEW* as described in the paper:<br>
> NEW: A Generic Learning Model for Tie Strength Prediction in Networks.<br>
The *NEW* algorithm mainly focuses on the link prediction of undirected graph weighted network

The experimental partition data required by the paper is stored under the data directory, which may be slightly deviated based on the operation of different machines.If you want to repartition the test data, please refer to the following instructions to complete the experimental results.

### Basic Usage

#### Example
To run *NEW* on celegans network, execute the following command from the project home directory:<br/>
	``python code/main.py --input ../data/celegans.csv --cache True --learning_rate 1e-7 --k 2.``
	
	
NetWork             | RMSE 10'th mean |
--------------------| :-------------: |
UC social           | 0.206±0.002     | 
C.elegans           | 0.137±0.003     | 
P.blogs             | 0.081±0.001     | 
NetScience          | 0.09±0.002      | 
Neural network      | 0.205±0.006     | 
Wiki                | 0.182±0.002     | 

#### Options
You can check out the other options available to use with *node2vec* using:<br/>
	``python code/main.py --help``
  
#### Input
The supported input format is an netwrok data:
	
    node1_id node2_id weight


### Miscellaneous

Please send any questions you might have about the code and/or the algorithm to <lee824002466@gmail.com>.

*Note:* This is only a reference implementation of the *NEW* algorithm and could benefit from several performance enhancement schemes, some of which are discussed in the paper.
