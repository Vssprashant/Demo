provider "azurerm"{
    version = "2.1"
    features{}
}

resource "azurerm_resource_group" "example"{
    name = "example"
    location = "India"
}

output "id" {
  value = data.azurerm_resource_group.example.id
}