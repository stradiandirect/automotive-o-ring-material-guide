"""
Reference O-ring material selector for automotive applications.

This is a simplified decision aid based on the framework in README.md.
It is NOT a substitute for compound-level datasheet review or engineering sign-off.

Usage:
    python material_selector.py --temp 150 --fluid gasoline_e10 --ozone true
"""

import argparse
import sys


def select_material(temp_c: float, fluid: str, ozone_exposed: bool) -> dict:
    """
    Return a recommended material family and reasoning.

    Args:
        temp_c: Continuous operating temperature in Celsius.
        fluid: One of 'oil', 'gasoline_e0', 'gasoline_e10', 'gasoline_e85',
               'diesel', 'coolant', 'brake_fluid', 'synthetic_oil'.
        ozone_exposed: True if the seal is exposed to ozone/UV.

    Returns:
        dict with 'recommendation', 'confidence', and 'reasoning'.
    """
    fluid = fluid.lower()

    aggressive_fluids = {"gasoline_e10", "gasoline_e85", "coolant", "brake_fluid"}
    standard_fluids = {"oil", "gasoline_e0", "diesel", "synthetic_oil"}

    if fluid not in aggressive_fluids | standard_fluids:
        return {
            "recommendation": "unknown",
            "confidence": "low",
            "reasoning": f"Fluid '{fluid}' not in reference dataset. Consult datasheet.",
        }

    # Rule 1: high temperature forces FKM
    if temp_c > 100:
        return {
            "recommendation": "FKM",
            "confidence": "high",
            "reasoning": f"Operating temp {temp_c}C exceeds NBR continuous limit (~100C).",
        }

    # Rule 2: ozone/UV exposure rules out NBR
    if ozone_exposed:
        return {
            "recommendation": "FKM",
            "confidence": "high",
            "reasoning": "Ozone/UV exposure degrades NBR. FKM required.",
        }

    # Rule 3: aggressive fluids favor FKM
    if fluid in aggressive_fluids:
        return {
            "recommendation": "FKM",
            "confidence": "medium",
            "reasoning": f"Fluid '{fluid}' is aggressive toward NBR. FKM preferred.",
        }

    # Rule 4: low temp narrows FKM choice
    if temp_c < -20:
        return {
            "recommendation": "NBR or low-temp FKM grade",
            "confidence": "medium",
            "reasoning": f"Temp {temp_c}C is below standard FKM limit. "
                         "NBR handles cold well; use low-temp FKM if heat resistance also needed.",
        }

    # Default: standard application
    return {
        "recommendation": "Buna-N (NBR)",
        "confidence": "high",
        "reasoning": f"Temp {temp_c}C and fluid '{fluid}' are within NBR envelope. "
                     "NBR is cost-effective and reliable here.",
    }


def main():
    p = argparse.ArgumentParser(description="Automotive O-ring material selector (reference).")
    p.add_argument("--temp", type=float, required=True, help="Continuous operating temp in Celsius")
    p.add_argument("--fluid", type=str, required=True,
                   help="oil | gasoline_e0 | gasoline_e10 | gasoline_e85 | diesel | coolant | brake_fluid | synthetic_oil")
    p.add_argument("--ozone", type=lambda x: x.lower() == "true", default=False,
                   help="true if exposed to ozone/UV")
    args = p.parse_args()

    result = select_material(args.temp, args.fluid, args.ozone)

    print(f"Recommendation : {result['recommendation']}")
    print(f"Confidence     : {result['confidence']}")
    print(f"Reasoning      : {result['reasoning']}")
    print()
    print("NOTE: Reference only. Verify against the specific compound datasheet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
