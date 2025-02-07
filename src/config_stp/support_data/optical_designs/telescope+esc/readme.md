### Design files for the telescope+ESC

ZOS file configs:
1. 2.4m cgraph science path
2. 1.2m cgraph science path
3. 1.2m cgraph FSM camera path
4. 2.4m cgraph FSM camera path
5. 1.2m cgraph LLOWFS path
6. 2.4m cgraph LLOWFS path
7. 6.5m full aperture SHWFS path
8. 6.5m full aperture acquisition camera path

### Associated Error Budgets

#### STP_Mark_12F11_Coronagraph_HC11_1
Although the optical design was updated, the ESC error budget is not updated at this time.
However, Heejoo wrote on 2024-01-30 via email, "The corresponding error budget table needs a new round tolerance simulation. Since newly added OAPs have similar focal lengths and off-axis distances, we might copy and paste the tolerance number from the identical OAP values."
Changes are therefore expected to be minor.

#### STP_Mark_12F11_HC03
The error budgets for these designs are still in development and are therefore not in this repository.
They can be found in the [spectrograph_design_docs](https://github.com/uasal/spacecoron_design_docs/tree/main/budgets/optical_design_wfe) repository and were merged on commit `f71d94d` on 2023-09-19.