# proton-calendar

A third-party python tool to access protonmail's calendar via API requests. This may eventually become a public python library includable via `pip install`.

---

## Dependencies

Install the Proton python client library:
`pip install proton-client`

Dependencies of that library are the following:

| **Python**                                                   | **Debian**       | **Fedora**        | **Arch**         |
| :----------------------------------------------------------- | :--------------- | :---------------- | :--------------- |
| [requests](https://github.com/psf/requests) >= 2.16.0 **\*** | python3-requests | python3-requests  | python-requests  |
| [bcrypt](https://github.com/pyca/bcrypt/)                    | python3-bcrypt   | python3-bcrypt    | python-bcrypt    |
| [python-gnupg](https://docs.red-dove.com/python-gnupg/)      | python3-gnupg    | python3-gnupg     | python-gnupg     |
| [pyopenssl](https://www.pyopenssl.org/en/stable/)            | python3-openssl  | python3-pyOpenSSL | python-pyopenssl |

_(See: https://github.com/ProtonMail/proton-python-client/blob/master/README.md)_
