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


## Code



