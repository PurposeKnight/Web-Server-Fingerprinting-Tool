# 🔐 **SSL Fingerprint Scanner**

A secure client–server application that performs fingerprint scans on target servers using **SSL/TLS encrypted communication**. The server handles multiple clients concurrently while ensuring secure communication through **self-signed certificates**.

---

## 📜 **SSL Certificate Setup**

Before starting the server, you must generate a **self-signed SSL certificate** to enable encrypted communication.

Run the following command in the **project root directory**:

```bash
openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes
```

---

## ⚠️ **Important**

`server.key` contains private keys and should **not be committed to version control**.

Add it to your `.gitignore` file:

```gitignore
server.key
```

---

## 💻 **Usage**

### **1️⃣ Start the Server**

Open a terminal and run:

```bash
./server
```

This will start the **secure listener waiting for client connections**.

---

### **2️⃣ Start the Client(s)**

Open another terminal (or multiple terminals to test concurrency):

```bash
./client
```

Each client will establish a **secure SSL connection with the server**.

---

### **3️⃣ Run a Fingerprint Scan**

When prompted by the client, enter the target server in the following format:

```
IP:PORT
```

#### **Examples**

```
Google: 142.250.193.206:80
Cloudflare: 1.1.1.1:80
```

---

## ❌ **Exit the Client**

To securely close the connection, type:

```
exit
```

---

## 🧪 **Testing Concurrency**

To test **multiple simultaneous connections**:

1. Start the server once  
2. Open multiple client terminals  
3. Run scans from each client  

The server will handle **all requests concurrently**.

---

## 📁 **Project Structure**

```
project-root/
│
├── server
├── client
├── server.crt
├── server.key        # ignored in git
├── README.md
└── .gitignore
```

---

## 🔒 **Security Note**

Private keys must **never be exposed in public repositories**.

Always include `server.key` in `.gitignore`.