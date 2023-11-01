# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccessPolicyEntry
from ._models_py3 import Attributes
from ._models_py3 import CheckNameAvailabilityResult
from ._models_py3 import CloudErrorBody
from ._models_py3 import DeletedVault
from ._models_py3 import DeletedVaultListResult
from ._models_py3 import DeletedVaultProperties
from ._models_py3 import DimensionProperties
from ._models_py3 import Error
from ._models_py3 import IPRule
from ._models_py3 import Key
from ._models_py3 import KeyAttributes
from ._models_py3 import KeyCreateParameters
from ._models_py3 import KeyListResult
from ._models_py3 import KeyProperties
from ._models_py3 import LogSpecification
from ._models_py3 import ManagedHsm
from ._models_py3 import ManagedHsmError
from ._models_py3 import ManagedHsmListResult
from ._models_py3 import ManagedHsmProperties
from ._models_py3 import ManagedHsmResource
from ._models_py3 import ManagedHsmSku
from ._models_py3 import MetricSpecification
from ._models_py3 import NetworkRuleSet
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import Permissions
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionItem
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import Resource
from ._models_py3 import ResourceListResult
from ._models_py3 import Secret
from ._models_py3 import SecretAttributes
from ._models_py3 import SecretCreateOrUpdateParameters
from ._models_py3 import SecretListResult
from ._models_py3 import SecretPatchParameters
from ._models_py3 import SecretPatchProperties
from ._models_py3 import SecretProperties
from ._models_py3 import ServiceSpecification
from ._models_py3 import Sku
from ._models_py3 import SystemData
from ._models_py3 import Vault
from ._models_py3 import VaultAccessPolicyParameters
from ._models_py3 import VaultAccessPolicyProperties
from ._models_py3 import VaultCheckNameAvailabilityParameters
from ._models_py3 import VaultCreateOrUpdateParameters
from ._models_py3 import VaultListResult
from ._models_py3 import VaultPatchParameters
from ._models_py3 import VaultPatchProperties
from ._models_py3 import VaultProperties
from ._models_py3 import VirtualNetworkRule

from ._key_vault_management_client_enums import AccessPolicyUpdateKind
from ._key_vault_management_client_enums import ActionsRequired
from ._key_vault_management_client_enums import CertificatePermissions
from ._key_vault_management_client_enums import CreateMode
from ._key_vault_management_client_enums import DeletionRecoveryLevel
from ._key_vault_management_client_enums import IdentityType
from ._key_vault_management_client_enums import JsonWebKeyCurveName
from ._key_vault_management_client_enums import JsonWebKeyOperation
from ._key_vault_management_client_enums import JsonWebKeyType
from ._key_vault_management_client_enums import KeyPermissions
from ._key_vault_management_client_enums import ManagedHsmSkuFamily
from ._key_vault_management_client_enums import ManagedHsmSkuName
from ._key_vault_management_client_enums import NetworkRuleAction
from ._key_vault_management_client_enums import NetworkRuleBypassOptions
from ._key_vault_management_client_enums import PrivateEndpointConnectionProvisioningState
from ._key_vault_management_client_enums import PrivateEndpointServiceConnectionStatus
from ._key_vault_management_client_enums import ProvisioningState
from ._key_vault_management_client_enums import Reason
from ._key_vault_management_client_enums import SecretPermissions
from ._key_vault_management_client_enums import SkuFamily
from ._key_vault_management_client_enums import SkuName
from ._key_vault_management_client_enums import StoragePermissions
from ._key_vault_management_client_enums import VaultProvisioningState
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessPolicyEntry",
    "Attributes",
    "CheckNameAvailabilityResult",
    "CloudErrorBody",
    "DeletedVault",
    "DeletedVaultListResult",
    "DeletedVaultProperties",
    "DimensionProperties",
    "Error",
    "IPRule",
    "Key",
    "KeyAttributes",
    "KeyCreateParameters",
    "KeyListResult",
    "KeyProperties",
    "LogSpecification",
    "ManagedHsm",
    "ManagedHsmError",
    "ManagedHsmListResult",
    "ManagedHsmProperties",
    "ManagedHsmResource",
    "ManagedHsmSku",
    "MetricSpecification",
    "NetworkRuleSet",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "Permissions",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionItem",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "Resource",
    "ResourceListResult",
    "Secret",
    "SecretAttributes",
    "SecretCreateOrUpdateParameters",
    "SecretListResult",
    "SecretPatchParameters",
    "SecretPatchProperties",
    "SecretProperties",
    "ServiceSpecification",
    "Sku",
    "SystemData",
    "Vault",
    "VaultAccessPolicyParameters",
    "VaultAccessPolicyProperties",
    "VaultCheckNameAvailabilityParameters",
    "VaultCreateOrUpdateParameters",
    "VaultListResult",
    "VaultPatchParameters",
    "VaultPatchProperties",
    "VaultProperties",
    "VirtualNetworkRule",
    "AccessPolicyUpdateKind",
    "ActionsRequired",
    "CertificatePermissions",
    "CreateMode",
    "DeletionRecoveryLevel",
    "IdentityType",
    "JsonWebKeyCurveName",
    "JsonWebKeyOperation",
    "JsonWebKeyType",
    "KeyPermissions",
    "ManagedHsmSkuFamily",
    "ManagedHsmSkuName",
    "NetworkRuleAction",
    "NetworkRuleBypassOptions",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "Reason",
    "SecretPermissions",
    "SkuFamily",
    "SkuName",
    "StoragePermissions",
    "VaultProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()