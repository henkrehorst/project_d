import os
from azure.storage.blob import ContainerClient, BlobClient, ContentSettings

def Upload(filename):
    azure_storage_connectionstring="DefaultEndpointsProtocol=https;AccountName=projectdimages;AccountKey=h30l1NRl/ROT4XqV6YEI+RCNl6MWzLPhjswBF5pl/pOFSF3sbsaW9qaIUqQxaDbgEAoEEfciErSaJBl9TFofFQ==;EndpointSuffix=core.windows.net"
    container_name = "images"
    source_folder = "./"

    #Set content type to png so it uploads the image as a png
    my_content_settings = ContentSettings(content_type='image/png')
    url = ""
    try:
        client_container = ContainerClient.from_connection_string(conn_str=azure_storage_connectionstring,container_name=container_name)
        blob = client_container.get_blob_client(filename)
        
        #If exits delete the existing 
        if blob.exists():
            blob.delete_blob()

        blob_client = BlobClient.from_connection_string(conn_str=azure_storage_connectionstring,container_name=container_name,blob_name=filename)
        

        with open(source_folder + filename + ".png","rb") as data:
            blob_client.upload_blob(data,content_settings=my_content_settings)

        url = blob_client.url
    except Exception as e:
        print(e)

    return url