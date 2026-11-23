from pathlib import Path

OUTPUT = Path("/output/entry.txt")

def main():
    email = """Subject: your invoices after a long week

Hey,

I know most guys in the trade are still sorting invoices and receipts on Sunday night after a full week of jobs. Quotes, materials, the cash ones, the ones that still haven’t been paid — it all just piles up.

I only do the bookkeeping side. Flat monthly fee. You send me pictures of the invoices and receipts (or just forward the emails) and I keep everything straight so tax time doesn’t turn into a mess. No new software to learn.

Want me to send a one-page example of what the monthly summary looks like? Takes about two minutes to look at between jobs.

Thanks,
Alex"""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(email.strip() + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
