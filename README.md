# openUC2 Modules Repository

Central repository for all UC2 module definitions — the digital twin layer connecting **OptiKit** (configurator), **Optiland** (optical simulation), **Autodesk Inventor** (CAD), and **ImSwitch** (microscope control).

## Architecture

```
 ┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌───────────┐
 │   OptiKit   │────▶│   Optiland   │────▶│  Inventor   │────▶│ ImSwitch  │
 │ Configurator│     │  Simulation  │     │    CAD      │     │  Control  │
 └──────┬──────┘     └──────┬───────┘     └──────┬──────┘     └─────┬─────┘
        │                   │                    │                   │
        └───────────────────┴────────────────────┴───────────────────┘
                                    │
                        ┌───────────┴───────────┐
                        │  THIS REPOSITORY      │
                        │  modules/ + schemas/  │
                        │  templates/ + scripts/│
                        └───────────────────────┘
```

## Quick Start

```bash
# Validate all modules
pip install jsonschema pyyaml
python scripts/validate_module.py

# Generate a new lens module from template
python scripts/generate_from_template.py \
  --category lens \
  --id lens-pcx-f75 \
  --params '{"focalLength_mm": 75, "diameter_mm": 25.4, "material": "N-BK7", "curvature_r2_mm": -38.8, "center_thickness_mm": 4.2, "vendor": "Thorlabs", "sku": "LA1608-A"}'

# Build configurator index
python scripts/build_configurator_index.py
```

## Repository Structure

```
openuc2-modules/
├── modules/                  # All module definitions
│   └── lens-pos-1x1/        # Example: plano-convex lens module
│       ├── module.yaml       # Master descriptor
│       ├── README.md
│       ├── docs/             # Datasheet, user manual, safety, etc.
│       ├── optics/           # Optiland JSON, Python model, CSYS
│       ├── cad/              # Inventor refs, exports (STL/STEP/GLB), BOM
│       ├── electronics/      # PCB, schematics (if applicable)
│       ├── firmware/         # CAN IDs, PlatformIO config (if applicable)
│       ├── software/         # ImSwitch config, drivers, state mapping
│       ├── configurator/     # Icons, thumbnails for web UI
│       ├── production/       # Print settings, supply chain
│       └── marketing/        # Photos, slides
├── templates/                # Parametric templates for Scenario 2
│   └── lens/                 # Lens category template
├── schemas/                  # JSON Schema validation files
├── scripts/                  # Build & automation scripts
├── vendor-catalogs/          # Raw vendor data for batch import
├── configurator/             # Built index for OptiKit web app
└── .github/workflows/        # CI/CD pipelines
```

## Three Onboarding Scenarios

| Scenario | When to Use | Entry Point | Automation Level |
|----------|-------------|-------------|------------------|
| **1. Handcrafted** | Custom/unique parts (galvo mounts, adapters) | Inventor CAD → Optiland → OptiKit | Low |
| **2. Generic** | Standard optics (lenses, mirrors, filters) | Parameters → Template → All | **High** (batch) |
| **3. External** | Manufacturer parts (spectrometers, cameras) | Specs → Optiland + Inventor → OptiKit | Medium |

## Cross-Repository References (UUIDs)

Every module has a stable UUID. External assets (Optiland models, CAD files) are referenced by UUID:

```yaml
optics:
  optiland_ref:
    repo: "https://github.com/openuc2/openuc2-optiland-models"
    uuid: "opt-a1b2c3d4-lens-pcx-50mm"    # Stable reference
    commit: "abc123"                        # Pin to specific version
```

This allows the configurator, simulation engine, and CAD tools to resolve the correct asset version without embedding large files in this repository.

## License

Hardware designs: **CERN-OHL-S-2.0** | Documentation: **CC-BY-SA-4.0** | Software/scripts: **MIT**
