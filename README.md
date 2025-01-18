# IPNow - Instant IP, Location & Network Details

![IPNow Logo](https://ipnow.rajayadav.in/static/images/ipnow_logo.png)

### Preview: [ipnow.rajayadav.in](http://ipnow.rajayadav.in)

---

## Overview
IPNow is a Flask-based web application that provides users with instant access to their public IP address, geolocation, and network information. Designed with simplicity and efficiency in mind, it offers a professional and user-friendly interface to meet the needs of both casual users and professionals.

---

## Key Features

- **Public IP Retrieval**: Instantly display your current public IP address.
- **Geolocation Details**: View city, region, country, and timezone information associated with your IP address.
- **Network Insights**: Access information about your Internet Service Provider (ISP).
- **Interactive Map**: Visualize your location on an embedded Google Map.
- **Responsive Design**: Optimized for seamless use across devices, including mobile, tablet, and desktop.

---

## Installation and Usage

Follow these steps to set up and run IPNow on your local machine:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/RajaYadav28/ipnow.git
    cd ipnow
    ```

2. **Install Dependencies**:
    Ensure Python (3.7 or later) is installed on your system. Install the required Python packages using:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    Start the Flask development server:
    ```bash
    python app.py
    ```
    Access the application in your browser at `http://127.0.0.1:5000`.

    **Note**: On a local setup, ensure the `REMOTE_ADDR` header in Flask points to the actual IP address by configuring proxies or network settings.

4. **Deploy (Optional)**:
    To deploy the application, you can use platforms like [Vercel](https://vercel.com), [Heroku](https://heroku.com), or [AWS](https://aws.amazon.com/).

---

## Configuration

1. **IP Data API**:
    - IPNow leverages the [IP-API](http://ip-api.com/) for fetching IP and location details.
    - To modify the API endpoint or parameters, edit the `get_fetch_ip_details` function in the `app.py` file.

2. **Static Assets**:
    - Customize the UI by updating or replacing images, styles, and scripts in the `static` folder.

3. **Environment Variables**:
    - Use environment variables to store sensitive data like API keys. Create a `.env` file in the root directory:
      ```
      API_URL=http://ip-api.com/json/
      FLASK_ENV=development
      ```

---

## Project Structure

- **app.py**: Main Flask application file handling routes and logic.
- **templates/**: Folder containing HTML templates for the web interface.
- **static/**: Directory for CSS, JavaScript, and image assets.
- **requirements.txt**: List of Python dependencies.

---

## Screenshots

### Homepage
![Homepage Screenshot](https://i.postimg.cc/Y0pj87tN/download.png)

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code. See the [LICENSE](LICENSE) file for full details.

### License Summary
- **Permissions**: Commercial use, modification, distribution, private use.
- **Conditions**: Include original copyright and license notice.
- **Limitations**: No liability or warranty is provided with the software.

---

## Contact

For queries, suggestions, or feedback, reach out:

- **Email**: [ry360596@gmail.com](mailto:ry360596@gmail.com)
- **Portfolio**: [rajayadav.in](http://www.rajayadav.in)

---

## Contributing

We welcome contributions to enhance IPNow! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with a meaningful message.
4. Open a pull request.

---

> Created with passion by [Developer Raja](https://www.rajayadav.in).

**Enjoy using IPNow! Your feedback and suggestions are always appreciated.**

