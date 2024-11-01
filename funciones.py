{{ secrets.SSH_PRIVATE_KEY }}

client = gradio_client.Client("Moibe/splashmix", hf_token=nodes.splashmix_token)