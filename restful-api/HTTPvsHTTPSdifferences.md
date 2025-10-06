# HTTP vs. HTTPS: The Core Difference

The key distinction between **HTTP** (Hypertext Transfer Protocol) and **HTTPS** (Hypertext Transfer Protocol Secure) is **security**.

* **HTTP** transmits data in **plain text**, making it vulnerable to interception and tampering. Think of it like sending a postcard – anyone can read it.
* **HTTPS** encrypts data using **SSL/TLS**, making it unreadable to unauthorized parties. This protects sensitive information and is essential for secure online interactions. It's like sending a letter in a sealed, tamper-proof envelope.

---

# HTTP Request and Response Outline

### HTTP Request

A client (e.g., your browser) sends an HTTP request to a server to ask for a resource or perform an action.

1.  **Request Line:**
    * **Method:** Action to perform (e.g., `GET`, `POST`).
    * **URI:** Resource path (e.g., `/index.html`).
    * **HTTP Version:** Protocol version (e.g., `HTTP/1.1`).

    ```
    GET /index.html HTTP/1.1
    ```

2.  **Headers:** Key-value pairs with additional info (e.g., `Host`, `User-Agent`).

    ```
    Host: [www.example.com](https://www.example.com)
    User-Agent: Mozilla/5.0 (Windows NT 10.0)
    ```

3.  **Message Body (Optional):** Data sent to the server (e.g., form data for `POST`).

    ```json
    {
        "username": "jimmycarrera",
        "password": "Mypassword"
    }
    ```

### HTTP Response

The server sends an HTTP response back to the client after processing the request.

1.  **Status Line:**
    * **HTTP Version:** Protocol version.
    * **Status Code:** Numeric result of the request (e.g., `200`, `404`).
    * **Reason Phrase:** Human-readable status description (e.g., `OK`, `Not Found`).

    ```
    HTTP/1.1 200 OK
    ```

2.  **Headers:** Key-value pairs with response info (e.g., `Content-Type`, `Date`).

    ```
    Content-Type: text/html; charset=UTF-8
    Content-Length: 1234
    ```

3.  **Message Body (Optional):** The requested resource or error message.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <h1>Welcome!</h1>
    </body>
    </html>
    ```

---

# Common HTTP Methods

HTTP methods define the action to be performed on a resource.

* **`GET`**: **Retrieves** data.
    * *Use Case:* Fetching a web page, getting data from an API.
* **`POST`**: **Submits** data to create or process a resource.
    * *Use Case:* Submitting a form, uploading a file.
* **`PUT`**: **Replaces** a resource or creates it if it doesn't exist.
    * *Use Case:* Fully updating a user's profile.
* **`DELETE`**: **Removes** a resource.
    * *Use Case:* Deleting a user account or an item.
* **`PATCH`**: **Applies partial modifications** to a resource.
    * *Use Case:* Updating only an email address in a user's profile.
* **`HEAD`**: Requests **headers only** for a resource, no body.
    * *Use Case:* Checking if a resource exists or its size without downloading it.
* **`OPTIONS`**: Describes the **communication options** for a resource.
    * *Use Case:* Pre-flight requests in CORS to check allowed methods.

---

# Common HTTP Status Codes

Status codes indicate the outcome of an HTTP request.

### 2xx Success

* **`200 OK`**: Request successful.
    * *Scenario:* A web page loads correctly.
* **`201 Created`**: New resource successfully created.
    * *Scenario:* A new user account is registered.
* **`204 No Content`**: Request successful, no content to return.
    * *Scenario:* A resource is successfully deleted.

### 3xx Redirection

* **`301 Moved Permanently`**: Resource permanently moved to a new URL.
    * *Scenario:* Redirecting `http://` to `https://`.
* **`302 Found`**: Resource temporarily moved.
    * *Scenario:* Redirecting to a login page after accessing a protected resource.
* **`304 Not Modified`**: Client's cached version is still valid.
    * *Scenario:* Browser uses a cached page, no need to re-download.

### 4xx Client Errors

* **`400 Bad Request`**: Server cannot understand the client's request (e.g., malformed syntax).
    * *Scenario:* Sending an API request with invalid data.
* **`401 Unauthorized`**: Client needs authentication.
    * *Scenario:* Accessing a protected page without logging in.
* **`403 Forbidden`**: Server refuses access, even with authentication.
    * *Scenario:* Trying to access a resource you don't have permissions for.
* **`404 Not Found`**: The requested resource does not exist.
    * *Scenario:* Trying to access a non-existent web page.
* **`405 Method Not Allowed`**: The HTTP method used is not supported for the resource.
    * *Scenario:* Trying to `POST` to a read-only endpoint.
* **`429 Too Many Requests`**: Client sent too many requests in a given time period.
    * *Scenario:* Exceeding an API's rate limit.

### 5xx Server Errors

* **`500 Internal Server Error`**: Generic server-side error.
    * *Scenario:* A bug in the server application.
* **`502 Bad Gateway`**: Server acting as a proxy received an invalid response from an upstream server.
    * *Scenario:* Backend server is down or unresponsive.
* **`503 Service Unavailable`**: Server is temporarily overloaded or down for maintenance.
    * *Scenario:* Website is undergoing planned downtime.
* **`504 Gateway Timeout`**: Server acting as a proxy didn't get a timely response from an upstream server.
    * *Scenario:* A backend API is taking too long to respond.