# Azure Functions Project with Storage Queue and SQL Output Bindings

This project showcases how to build and deploy Python-based Azure Functions that:

- Push messages to an Azure Storage Queue  
- Add entries to an Azure SQL Database  

Both functions were developed locally in Visual Studio Code, tested on a development machine, and successfully deployed to Azure.

## ✅ Tasks Accomplished

### 1. Output Binding to Azure Storage Queue
- Followed Microsoft’s QuickStart guide for the Storage Queue output binding.  
- Used Python and VS Code for building and testing.  
- Validated the function locally using both REST API calls and `curl`.  
- Deployed to Azure and confirmed that messages were successfully sent to `outqueue` via Azure Storage Explorer.

### 2. Output Binding to Azure SQL Database
- Used Microsoft’s QuickStart for Azure SQL bindings.  
- Set up `mySampleDatabase` with a table named `dbo.ToDo`.  
- Confirmed successful insertions triggered by HTTP requests using the Azure Query Editor.

## ⚙️ Environment Configuration

### Azure Services Provisioned

 Azure Storage                    
 Azure Queue                         |
 Azure SQL Database           |
 SQL Server          
 Function App        

### Local Development Requirements
- Python version 3.8 or 3.9  
- Azure Functions Core Tools installed  
- VS Code with the following extensions:  
  - Python  
  - Azure Functions  
  - Azure Storage  
- Azure Storage Explorer  
- (Optional) Azurite for emulating queue storage locally

## 📦 Steps to Begin Development

1. Open your project folder in VS Code or create a new Azure Functions project.  
2. Sync cloud configuration to your local machine:  
   - Press `F1` → select **Azure Functions: Download Remote Settings...**  
   - Choose your deployed Function App  
   - Confirm when asked to replace `local.settings.json`  
   - Copy the updated `AzureWebJobsStorage` string for local testing
