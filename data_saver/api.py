import requests


def get_batch_sales_data(url: str, token: str, sales_date: str, page: int) -> dict:
    """get batch of sales (one page)"""

    payload = {'page': page, "date": sales_date}
    header = {'Authorization': token}

    response = requests.get(
        url=f"{url}/sales",
        params=payload,
        headers=header
    )

    return {"data_response": response.json(), "status_code": response.status_code}


def get_sales(url: str, token: str, sales_date: str) -> list:
    """get sales batch by batch and return list of all of them"""

    sales_list = []
    status = 200
    page = 1

    while status == 200:
        batch_data = get_batch_sales_data(url=url, token=token, sales_date=sales_date, page=page)
        status = batch_data["status_code"]

        if status == 200:
            sales_data = batch_data["data_response"]
            sales_list.extend(sales_data)

        page += 1

    return sales_list
