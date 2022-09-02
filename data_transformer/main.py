from data_saver import get_exchange_rate
from common import notify_tg
from data_to_sheet import write_data


target_note = get_exchange_rate(bank='mono')
notify_tg(target_note)

write_data(target_note)
notify_tg('it`s done 👌')


def main():
    pass


if __name__ == "__main__":
    main()
