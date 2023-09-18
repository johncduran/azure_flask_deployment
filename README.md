# azure_flask_deployment
azure flask deployment

## Azure URL
Here is the url for the deployed web app using Azure services 
john-504-flask.azurewebsites.net

### Step 1: Installation
First I installed the Azure CLI using the bash command: ‘curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash ‘ This command was provided in Azure’s documentaation located here https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt. 

### Step 2: Login
Then I made sure that it was installed correctly by typing the Google shell terminal ‘az’. 
After that, I then used the command ‘az login --use-device-code’ in order to login into my Azure account through the terminal. I had to click a link that was provided after typing in the command and then put in a code provided to me by the terminal. 

### Step 3: Setup
Later on I typed in ‘az account list --output table’ and this provided me three different cloud names under my Azure account where I could see which was the default one. I then changed it to my ‘Azure for Students’ one using its unique subscription ID. 

### Step 4 Deployment
I then went into the Azure web portal to create a resource group called John504. I then ran the command ‘az webapp up --name john-504-flask --runtime PYTHON:3.9 --sku B1’ in order to deploy my app onto the Azure cloud. 

After some time of loading it finally uploaded and was given its own domain name called john-504-flask.azurewebsites.net. 
