### Opto-Mechanical Design Reference Drawing

INST-0200.pdf is the system-level opto-mechanical Design Reference Drawing that should be used as the reference when describing the opto-mechanical system.
The detailed optical parameters are as-designed and therefore are expected to change after fabrication.
The spacing between the optics is not expected to change, except to compensate for any fabrication errors.

### Optical design files for only the telescope


#### STP_TMA_13_03

Updates to model:
- M4 mechanical diameter updated: 110 mm, CA 100 mm 
- Apply detector rect aperture on detector plane: 400 x 155 mm (original field range coverage). This needs to be updated when the WCC layout study is completed. 

Additions:
Added information that calculated to ensure consistency with values in INST-0200.
- IFS feed field: refer to Doug's WCC array
- field angle: (-0.070250,-3.5e-4)
- WCC position: (120.0204,0.003)

#### STP_TMA_13_02
Never released

#### STP_TMA_13_01

This update to the design is to remove significant figures that were beyond measurement and tolerance capabilities.
It was also used as the basis to producing INST-0200, the first iteration of a the opto-mechanical Design Reference Drawing.

#### STP_TMA_Mark_12F+M1_Bending (deprecated)

This file should be the exact same as Daewook's original STP_TMA_Mark_12F design except M1 is a Zernike sag surface for inputting M1 bending mode corrections.

ZOS file configs:
1. 6.5m full aperture 
2. 2.4m sub-aperture

### Associated Error Budgets

#### STP_TMA_13_03
No change to error budget required.

#### STP_TMA_13_02
Not released

#### STP_TMA_13_01
The recent update of the optical design from STP_TMA_Mark_12F+M1_Bending to STP_TMA_13_01 has no changes to the WFE budget.

#### STP_TMA_Mark_12F+M1_Bending

The error budgets for these designs are still in development and are therefore not in this repository.
They can be found in the [spectrograph_design_docs](https://github.com/uasal/spacecoron_design_docs/tree/main/budgets/optical_design_wfe) repository and were merged on commit `f71d94d` on 2023-09-19.
