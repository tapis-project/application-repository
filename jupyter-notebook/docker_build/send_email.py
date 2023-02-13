import argparse
import smtplib

host = 'relay.tacc.utexas.edu'
port = 25

def send_email(email, message):
    sender_email = "no-reply@tacc.cloud"
    receiver_email = email

    try:
        server = smtplib.SMTP(host, port)
        server.sendmail(sender_email, receiver_email, message)
        print("SUCCESS")
    except Exception as e:
        print(f'ERROR: {e}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('email', metavar='EMAIL', type=str, help='Email address')
    parser.add_argument('message', metavar='MESSAGE', type=str, help='Message to send')
    args = parser.parse_args()
    send_email(args.email, args.message)

if __name__ == "__main__":
    main()