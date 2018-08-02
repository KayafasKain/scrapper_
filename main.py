import argparse
import sys
from core import habr_scrapper as has



# hs = hs.HabrScrapper('https://habr.com/')
# hs.start()

def main():

    parser = argparse.ArgumentParser(
        description='habr parser'
    )

    parser.add_argument(
        '--list-url',
        metavar='URL',
        type=str,
        required=False,
        help='link to list of posts',
    )

    parser.add_argument(
        '--outfile',
        metavar='FILE',
        type=str,
        required=False,
        help='outfile name',
    )

    args = parser.parse_args()

    if args.list_url:
        if args.outfile:
            hs = has.HabrScrapper(args.list_url, args.outfile)
        else:
            hs = has.HabrScrapper(args.list_url)
        hs.start()
    else:
        link = input('enter url: ')
        filename = input('enter filename (optional): ')
        if args.outfile:
            hs = has.HabrScrapper(link, filename)
        else:
            hs = has.HabrScrapper(link)
        hs.start()

if __name__ == "__main__":
    sys.exit(main())
