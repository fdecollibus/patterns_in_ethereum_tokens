# Patterns and Centralisation in Ethereum Based Token Transaction Networks

Repository with code from the paper "Patterns and Centralisation in Ethereum Based Token Transaction Networks", which is currently under review.

## Article Abstract
We explore patterns, regularities, and correlations in the evolving landscape of Ethereum based tokens, both ERC-20 (fungible) and ERC-721 (non fungible) with the aim of understanding the factors contributing to the rise of certain tokens over others. By applying network science methodologies, minimum spanning trees, econometric ARMA models, and the study of accumulation processes we are able to highlight a rising centralisation process. Not only ``rich" tokens get richer, but past transactions also emerge as more reliable predictors of new transactions. Our findings are validated across different samples of tokens.

## Data

The exact data to run to repeat the experiments can be made available under request. Please contact francesco.decollibus@business.uzh.ch 

### Extract Token Transfers
It is possible to independently collect the data used in this paper. For this paper, ethereum-etl tool has been used. You have two options:
1. Download the [Dataset](https://cloud.google.com/blog/products/data-analytics/introducing-six-new-cryptocurrencies-in-bigquery-public-datasets-and-how-to-analyze-them)  directly from [Google Cloud](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=crypto_ethereum&page=dataset). 
2. Run a fully synchronized Ethereum Node, download [ethereum-etl](https://github.com/blockchain-etl/ethereum-etl) tool and run the [*extract_token_transfers*](https://ethereum-etl.readthedocs.io/en/latest/commands/#extract_token_transfers)  method. 

In any case after you extracted the data, you will need to aggregate them using the token_address column.

### Sample Data
For convenience in order to test and run the script, two very small samples are provided, from block 18900000 to 18900100. The real data used for the paper should be almost 1 tb.
+ sample_data/sample_block_transfer.csv with the token transfers for this 100 blocks. Sample data.
+ sample_data/sample_block_timestamp.csv with the pertaining block to timestamp mapping. Sample data.
+ sample_data/dictionary_token_red.pickle a reduced dictionary of only the tokens that have been used in the analysis. They are used in some scripts.

We included as well two complete data sets from the paper:
+ sample_data/cumsum_results_cs.npz.zip this file is used for rank calculation. Remember to unzip before usage. 
+ sample_data/overall_count_lines.npy.zip this file is used for power law fits (see the jupyter notebook). Remember to unzip before usage.

## Code
The code assume a fixed folder structure, where tokens are handled in a folder called "token_data", change everything accordingly. Install the requirements as in requirements.txt

### Preparation

#### First step: preparing your data
Assuming you have a token_transfer.csv file, you first need to prepare your data. Adapt the path and the folders in the script files accordingly
1. Run *1_recompose_token.py*: this script will split the token transfers throughout different folders pro token addresses. The transfers will still be unordered
2. Run *2_sort_files.py*: this script will sort the token transfers in every subfolder.
3. Run *3_create_dictionary.py*: it will create a dictionary file for the tokens, to be referenced when populating arrays in the following steps

#### Second step: networks, sets of edges and nodes 
1. Run *4_create_network_sets_for_jaccard.py*: this will create sets of edges and nodes pro tokens for further usage in the jaccard index

#### Third step: prepare daily time series for new daily transactions
1. Run *5_prepare_tx_time_series.py*
2. Run *6_setup_tx_time_series.py*
3. Run *7_run_tx_time_series.py*

### Analysis

#### Compute the Jaccard Index for nodes and edges
1. Run *8_compute_jaccard.py*

#### Compute the correlation matrix for added new transactions
1. Run *9_compute_tx_correlation_matrix.py*

#### Compute the correlation Tree for MST
1. Run *10_mst_builder_transactions.py*

#### Compute the ARMA Parameters
1. Run *11_compute_arma_parameters.py*

#### Run the rank analysis
Complete data are present in the sample_data folder
1. Prepare the data with *12_prepare_for_rank_analysis.py*
2. Run the analysis with *13_compute_rank.py*

#### Run the power law fits and plots
Complete data are present in the sample_data folder
1. You have a jupyter notebook *14_powerlaw_plotter_2024.ipynb*


# Problems or Q&A
Please contact me or open an issue.
   





