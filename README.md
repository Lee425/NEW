# NEW

This repository provides a reference implementation of *NEW* as described in the paper:<br>
> NEW: A Generic Learning Model for Tie Strength Prediction in Networks.<br>
The *NEW* algorithm mainly focuses on the link prediction of undirected graph weighted network

The experimental partition data required by the paper is stored under the data directory, which may be slightly deviated based on the operation of different machines.If you want to repartition the test data, please refer to the following instructions to complete the experimental results.

### Basic Usage

#### Example
To run *NEW* on celegans network, execute the following command from the project home directory:<br/>
	``python code/main.py --input ../data/celegans.csv --cache True --learning_rate 1e-5 --k 2.``
	
	
NetWork             | RMSE 10'th mean |
--------------------| :-------------: |
UC social           | 7.31±1.04       | 
C.elegans           | 1.5±0.63        | 
P.blogs             | 0.34±0.01       | 
NetScience          | 0.22±0.06       | 
Neural network      | 5.27±0.71       | 
Wiki                | 8.79±0.73       | 

#### Options
You can check out the other options available to use with *node2vec* using:<br/>
	``python code/main.py --help``
  
#### Input
The supported input format is an netwrok data:
	
    node1_id node2_id weight


### Miscellaneous

Please send any questions you might have about the code and/or the algorithm to <lee824002466@gmail.com>.

*Note:* This is only a reference implementation of the *NEW* algorithm and could benefit from several performance enhancement schemes, some of which are discussed in the paper.
