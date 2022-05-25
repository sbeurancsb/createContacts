import pandas as p
import numpy as np
import requests as r
from datetime import datetime, timezone


class Payload:
    def __init__(self, fields):
        self.fields = fields

    def build(outlet_id, name, email, favorite, job_title, phone):
        # get contact info
        fields = {}
        fields["outletId"] = outlet_id
        fields["name"] = name
        fields["email"] = email
        fields["favorite"] = favorite
        fields["jobTitle"] = job_title
        fields["phone"] = phone
        fields["modificationDate"] = fields["creationDate"] = datetime.isoformat(datetime.now(timezone.utc))[:-6]+"Z"
        return Payload(fields)

def main():
    #fill with AUTH TOKEN
    URL = ("https://api.tst.carlsbergwebservices.com/cadi/api/contacts") 
    AUTH_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBUUdJcE16a19tREhsNmpndEQ4TjNldnVsZndldUJRTUdnQkRtVUNNLWc0In0.eyJqdGkiOiJkY2FjZmM4YS0wNWVhLTRkOWYtYjA4ZC01ODY2ZTI0N2RmODIiLCJleHAiOjE2NTM0MTQ3MDcsIm5iZiI6MCwiaWF0IjoxNjUzNDExMTA3LCJpc3MiOiJodHRwczovL2NhZGkudHN0LmN4LWFwcHMuaW8vYXV0aC9yZWFsbXMvY3giLCJhdWQiOlsiYnJva2VyIiwiYWNjb3VudCJdLCJzdWIiOiI4YzRjZDA1Mi02YjBlLTQ0YmYtODg2MS01ZmUyYzViYjBiZDEiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJjeC1hcHBzIiwibm9uY2UiOiJhNjFjZTM4Ny0zMTFhLTQ4ODMtYjYzOS01Njc5MzhiM2E3MzIiLCJhdXRoX3RpbWUiOjE2NTMwMTE3MjQsInNlc3Npb25fc3RhdGUiOiJiNGM1ZmI0NS1hOGU1LTQ1ODItODFjMi1hMWI1ZTY0OTEyNDQiLCJhY3IiOiIwIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJicm9rZXIiOnsicm9sZXMiOlsicmVhZC10b2tlbiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQiLCJjeCI6eyJ0ZXAiOltdLCJ1c2VyRGF0YSI6eyJ0eXBlIjoiSU5URVJOQUwiLCJkZXRhaWxzIjp7ImVpZCI6ImJjZjAyNTRjLTAxMzEtNGZjOC04NTYzLTc0MTk0NWU3YWE0MyIsImZpcnN0TmFtZSI6IlNhbXVlbCIsImxhc3ROYW1lIjoiQmV1cmFuIiwiZW1haWxzIjpbeyJkZWZhdWx0RW1haWwiOnRydWUsImFkZHJlc3MiOiJzYW11ZWwuYmV1cmFuQGNhcmxzYmVyZ2dyb3VwLmNvbSIsImlzRGVmYXVsdEVtYWlsIjp0cnVlfV0sInBob25lcyI6W10sInJvbGVzIjp7InVzZXJSb2xlcyI6W3sicm9sZSI6eyJhcHBsaWNhdGlvbkNvZGUiOiJBTEwiLCJyb2xlTmFtZSI6IkFETUlOIn19XSwidXNlclNhbGVzT3JnUm9sZXMiOlt7InJvbGUiOnsiYXBwbGljYXRpb25Db2RlIjoiQ0FESSIsInJvbGVOYW1lIjoiQURNSU4ifSwic2FsZXNPcmdDb2RlIjoiRDAwMSJ9LHsicm9sZSI6eyJhcHBsaWNhdGlvbkNvZGUiOiJDQURJIiwicm9sZU5hbWUiOiJBUFBfT1JERVJfVVNFUiJ9LCJzYWxlc09yZ0NvZGUiOiJBMDAxIn0seyJyb2xlIjp7ImFwcGxpY2F0aW9uQ29kZSI6IkNBREkiLCJyb2xlTmFtZSI6IkFQUF9PRlRfU1VQX1VTRVIifSwic2FsZXNPcmdDb2RlIjoiQTAwMSJ9LHsicm9sZSI6eyJhcHBsaWNhdGlvbkNvZGUiOiJDQURJIiwicm9sZU5hbWUiOiJCT19PRlRfVVNFUiJ9LCJzYWxlc09yZ0NvZGUiOiJBMDAxIn1dLCJ1c2VyU2FsZXNPcmdDdXN0b21lclJvbGVzIjpbXX19LCJleHRyYURldGFpbHMiOnsiYXp1cmVVc2VyRGV0YWlscyI6eyJjb3VudHJ5IjoiUG9ydHVnYWwiLCJ1c2FnZUxvY2F0aW9uIjoiUFQiLCJjeEdyb3VwcyI6WyJDWF9DQURJX0FDQ0VTUyIsIkNYX0NBRElfQUNDRVNTX0RFViIsIkNYX0NBRElfQUNDRVNTX1NURyIsIkNYX0NBRElfQUNDRVNTX1RFU1QiLCJDWF9DQURJX09SREVSX1NURyIsIkNYX0NBRElfT1JERVJfREVWIiwiQ1hfQ0FESV9PUkRFUiJdfX19fX0.r59xY73jn0wfIA-FSnJZGmyP_NqVQeOTDg9xDu1cljIDvjcxKdYr6zU-lppBZuZoIctHuDF7AGPV-gj5l1MX0sDXxqOIunHKSQsNL4kaw613R6bF37se5R0PH_1ahyBwGj92004AOGqFDcTYYZBrEXF3VQ99P0Vi0sT3aR4JL8FicDf5ppl3j1nuaAbp5p5v4zcBJSVFpDfmQQoDXDkL-Ud8xG6o5R0I-JOWctblSLSPoSM5Ofr_xd_iS6di2haaxdaaneN5wDYYYoFClCY1edXIfHmTPPuIjT3TtpofVcg30h_gR4-gQfUzZ8JBRIISpA3dwZ2-u4vT_kGlURv7FQ"
    HED = {'Authorization': 'Bearer ' + AUTH_TOKEN}


    df = p.read_excel("Contactpersons1.xlsx").replace({np.nan: ""})

    for i, row in df.iterrows():
        # looping through data row by row
        payload = Payload.build(
            outlet_id = row["customerId"],

            name = row["Name"],
            email = row["E-Mail Address                    "], # these extra spaces are here to grab the column, since the excel file also has these
            favorite = False,
            job_title = { # not sure what needs to go in this section, so I just manually populated it
                "name": "Butiksassistent",
                "salesOrgCode": "A001",
                "isOnTrade": False,
                "createdDate": "2021-12-02T11:13:42",
                "modifiedDate": "2021-12-02T11:13:42",
                "createdBy": "ADMIN",
                "modifiedBy": "ADMIN",
                "createdByApp": "cx-contact-services",
                "modifiedByApp": "cx-contact-services",
                "id": "80dc6007-683f-4b7a-ac6e-8db3365d3c55"
                },
            phone = row["Telephone"],
            )
        # Now you can send the payload to the server
        response = r.post(URL, json=payload.fields, headers=HED)
        print(f"Row {i+1}, Name: {row['Name']}") # This will help you find what row gave you the response
        print(response.status_code)
        print(response.request.body)
        print(response.reason)
        print(response.json)



if __name__ == "__main__":
    main() # To run this, its the same as you normally did `python python_file.py`

# Sample output:
# {
# 	"outletId": 6001487,
# 	"name": "Ole ...",
# 	"email": null,
# 	"favorite": false,
# 	"jobTitle": {
# 		"name": "Butiksassistent",
# 		"salesOrgCode": "A001",
# 		"isOnTrade": false,
# 		"createdDate": "2021-12-02T11:13:42",
# 		"modifiedDate": "2021-12-02T11:13:42",
# 		"createdBy": "ADMIN",
# 		"modifiedBy": "ADMIN",
# 		"createdByApp": "cx-contact-services",
# 		"modifiedByApp": "cx-contact-services",
# 		"id": "80dc6007-683f-4b7a-ac6e-8db3365d3c55"
# 	},
# 	"phone": null,
# 	"modificationDate": "2022-05-21T15:56:08.966562Z",
# 	"creationDate": "2022-05-21T15:56:08.966562Z"
# }