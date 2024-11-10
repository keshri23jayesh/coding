import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# AWS SES SMTP credentials
SMTP_USERNAME = ''  # Replace with your AWS SES SMTP username
SMTP_PASSWORD = ''  # Replace with your AWS SES SMTP password

# AWS SES SMTP server information
SMTP_HOST = 'email-smtp.us-east-1.amazonaws.com'  # Replace with your region's SMTP server
SMTP_PORT = 587  # For TLS

# Email details
from_email = 'security@permi.tech'  # Replace with your verified email in AWS SES
to_email = 'jayeshkeshri70@gmail.com'
subject = 'Test Email from AWS SES'
body_text = 'Hello Jayesh, This is a test email sent using AWS SES SMTP credentials.'
body_html = """
<html>
<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      color: #333333;
      background-color: #f9f9f9;
      margin: 0;
      padding: 0;
    }
    .container {
      width: 100%;
      max-width: 600px;
      margin: 20px auto;
      background-color: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .logo {
      text-align: center;
      margin-bottom: 20px;
    }
    .logo img {
      width: 60px;
    }
    .content h2 {
      font-size: 24px;
      color: #333333;
    }
    .content p {
      font-size: 16px;
      color: #666666;
      line-height: 1.5;
    }
    .content a {
      color: #1e88e5;
      text-decoration: none;
    }
    .footer {
      text-align: center;
      font-size: 12px;
      color: #999999;
      margin-top: 20px;
    }
    .footer a {
      color: #1e88e5;
      text-decoration: none;
    }
    .download-buttons img {
      width: 140px;
      margin: 10px 5px;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="logo">
      <img src="https://permitech.s3.amazonaws.com/64c7183cb803__[PROXY]" alt="Presto Logo">
    </div>
    <div class="content">
      <h2>Thank you for your payment!</h2>
      <p>Hi [username],</p>
      <p>We have successfully processed payment for your recurring Professional team (monthly) subscription to Presto Labs. You can find your receipt <a href="#">here</a>.</p>
      <p><strong>Invoice ID:</strong> in_1QdkHtlvcqWR3dFD95WuKImu<br>
      <strong>Team:</strong> ACME Corp’s team<br>
      <strong>Start:</strong> Oct 25, 2024<br>
      <strong>End:</strong> Nov 25, 2024<br>
      <strong>Total:</strong> £28.00 GBP</p>
      <p>You can manage your bill by visiting the <a href="#">Admin settings</a>.</p>
    </div>
    <hr style="border: none; border-top: 1px solid #eeeeee; margin: 20px 0;">
    <div class="content">
      <p style="text-align: center;">Questions or concerns? Get in touch with us at <a href="mailto:support@prestolabs.ai">support@prestolabs.ai</a> or <a href="#">Discord</a>.</p>
      <p style="font-size: 14px; text-align: center; color: #666666;">
        Permitech safety management platform empowers industrial operators to minimize safety incidents, identify risks, and improve process efficiency.
      </p>
    </div>
    <div class="download-buttons" style="text-align: center;">
      <p><strong>Never miss an update</strong></p>
      <p>Download and install our new mobile app.</p>
      <a href="#"><img src="https://permitech.s3.amazonaws.com/64c7183cb803__[PROXY]" alt="App Store"></a>
      <a href="#"><img src="https://permitech.s3.amazonaws.com/64c7183cb803__[PROXY]" alt="Google Play"></a>
    </div>
    <div class="footer">
      <p>Want to change how you receive these emails? You can <a href="#">unsubscribe</a> or <a href="#">manage your email preferences</a>.</p>
      <p>7 Bell Yard, London, WC2A 2JR<br>United Kingdom</p>
      <div style="margin-top: 10px;">
        <a href="#"><img src="https://permitech.s3.amazonaws.com/64c7183cb803__[PROXY]" alt="LinkedIn" style="width: 20px; margin-right: 10px;"></a>
        <a href="#"><img src="https://permitech.s3.amazonaws.com/64c7183cb803__[PROXY]" alt="Discord" style="width: 20px; margin-right: 10px;"></a>
        <a href="#"><img src="https://permitech.s3.amazonaws.com/64c7183cb803__[PROXY]" alt="YouTube" style="width: 20px;"></a>
      </div>
    </div>
  </div>
</body>
</html>

"""


def send_email():
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body

    msg.attach(MIMEText(body_text, 'plain'))
    msg.attach(MIMEText(body_html, 'html'))

    # Connect to the SMTP server using TLS
    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    server.starttls()

    # Login to the SMTP server
    server.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())

    # Close the connection
    server.quit()

    print(f"Email sent to {to_email}.")

if __name__ == "__main__":
    send_email()
