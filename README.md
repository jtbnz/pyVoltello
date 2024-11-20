# pyVoltello
testing for python access to Voltello

## Setup

### get an api key
https://github.com/villageenergy/ve-public-api/discussions/2


### Creating the `config.py` File

To run this project, you need to create a `config.py` file in the root directory of the project. This file will store your API token. Follow these steps:

1. Create a new file named `config.py` in the root directory.
2. Add the following lines to the `config.py` file:

    ```python
    # config.py
    API_TOKEN = "YOUR_API_TOKEN" 
    CUSTOMER_ID = "YOUR CUSTOMER ID"
    UTILITY_ID = "YOUR UTILITY ID"
    ```

3. Replace `"YOUR_API_TOKEN"` with your actual API token.

Your `config.py` file should look like this:

```python
# 
API_TOKEN = "YOUR_API_TOKEN" # This is obtained from the Mobile App
CUSTOMER_ID = "YOUR CUSTOMER ID" # Not sure how to get this yet
```

### References

https://docs.devices.village.energy/ve-x-api/index.html#/

