import requests


def get_batch_sales_data(url: str, token: str, sales_date: str, page: int) -> dict:
    """get batch of sales (one page)"""
    data_response = requests.get(
        url=f"{url}/sales?date={sales_date}&page={page}",
        headers={'Authorization': token}
    )

    return data_response.json()


def get_sales(url: str, token: str, sales_date: str) -> list:
    """get sales batch by batch and return list of all of them"""

    sales_list = []
    for page in range(1, 100, 1):
        """Set limit for pages we are ready to process: 100"""
        batch_data = get_batch_sales_data(url=url, token=token, sales_date=sales_date, page=page)

        if type(batch_data) == list and type(batch_data[-1]) == dict and "client" in batch_data[-1]:
            sales_list.extend(batch_data)
        else:
            break

    return sales_list
