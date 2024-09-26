# Patterns and Centralisation in Ethereum Based Token Transaction Networks

Repository with the code from the paper "Patterns and Centralisation in Ethereum Based Token Transaction Networks", which is currently under submission process.

## Article Abstract
We explore patterns, regularities, and correlations in the evolving landscape of Ethereum based tokens, both ERC-20 (fungible) and ERC-721 (non fungible) with the aim of understanding the factors contributing to the rise of certain tokens over others. By applying network science methodologies, minimum spanning trees, econometric ARMA models, and the study of accumulation processes we are able to highlight a rising centralisation process. Not only ``rich" tokens get richer, but past transactions also emerge as more reliable predictors of new transactions. Our findings are validated across different samples of tokens.

## Data

The precise data to run the experiment will be made available under requests. Please write to francesco.decollibus@business.uzh.ch 
For token transfer the order to be followed 
### Extract Token Transfers
For this paper, ethereum-etl tool has been used. You have two options:
1. Download the [Dataset](https://cloud.google.com/blog/products/data-analytics/introducing-six-new-cryptocurrencies-in-bigquery-public-datasets-and-how-to-analyze-them)  directly from [Google Cloud](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=crypto_ethereum&page=dataset). 
2. Run a fully synchronized Ethereum Node, download [ethereum-etl](https://github.com/blockchain-etl/ethereum-etl) tool and run the [*extract_token_transfers*](https://ethereum-etl.readthedocs.io/en/latest/commands/#extract_token_transfers)  method. 

In any case after you extracted the data, you will need to aggregate them using the token_address column.

### Sample Data
For convenience in order to test and run the script, two very small samples are provided, from block 18900000 to 18900100. The real data used for the paper should be almost 1 tb.
+ sample_data/sample_block_transfer.csv with the token transfers for this 100 blocks 
+ sample_data/sample_block_timestamp.csv with the pertaining block to timestamp mapping

## Code
The code assume a fixed folder structure, where tokens are handled in a folder called "token_data", change everything accordingly. Install the requirements as in requirements.txt

### First step: preparing your data
Assuming you have a token_transfer.csv file, you first need to prepare your data. Adapt the path and the folders in the script files accordingly
1. Run *1_recompose_token.py*: this script will split the token transfers throughout different folders pro token addresses. The transfers will still be unordered
2. Run *2_sort_files.py*: this script will sort the token transfers in every subfolder.
3. Run *3_create_dictionary.py*: it will create a dictionary file for the tokens, to be referenced when populating arrays in the following steps

### Second step: networks and Jaccard index
1. Run *4_create_sets_for_jaccard.py*: this will create sets of edges and nodes pro tokens for further usage in the jaccard index




