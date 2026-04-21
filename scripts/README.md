# Project Maintenance Scripts

These Python utilities are used to maintain the architectural integrity of the trilingual AI and Digital Capacity Building framework.

## 1. `audit_links.py`
Performs a comprehensive audit of all HTML files in the repository.
- **Checks for:** Broken relative paths, missing files, and empty `href="#"` links.
- **Usage:** 
  ```bash
  python3 scripts/audit_links.py
  ```

## 2. `standardize_links.py`
A powerful repair utility that enforces site-wide consistency.
- **Actions:** 
  - Corrects relative paths for all assets (CSS, Images, Favicon).
  - Standardizes the `lang-selector` (top-right) to link to corresponding pages in all 3 languages.
  - Links breadcrumbs (e.g., "DigiTruck >") to the correct localized index.
  - Ensures the header logo links to the correct localized home portal.
- **Usage:**
  ```bash
  python3 scripts/standardize_links.py
  ```

---
**Note:** Always run `audit_links.py` after making structural changes or adding new modules to ensure a 100% functional user experience.
