"""
Zero Trust Network Access (ZTNA) — Educational Access Gateway Simulator
Prepared for: Shivraj Jarupla

This is a classroom simulation. It does not connect to real identity providers,
devices, networks, or security infrastructure.
"""

from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    STEP_UP = "ADDITIONAL VERIFICATION REQUIRED"


@dataclass
class AccessRequest:
    user: str
    role: str
    resource: str
    device_managed: bool
    mfa_verified: bool
    risk_score: int  # 0 = low risk, 100 = high risk


# Example least-privilege policy: roles are granted access only to named resources.
ROLE_RESOURCES = {
    "student": {"learning-portal", "library"},
    "staff": {"learning-portal", "library", "staff-dashboard"},
    "admin": {"learning-portal", "library", "staff-dashboard", "security-console"},
}


def evaluate_access(request: AccessRequest) -> tuple[Decision, str]:
    """Evaluate a request using identity, resource, device, MFA, and risk signals."""
    if request.role not in ROLE_RESOURCES:
        return Decision.DENY, "Unknown role; default-deny policy applies."

    if request.resource not in ROLE_RESOURCES[request.role]:
        return Decision.DENY, "Role is not authorized for this resource."

    if not 0 <= request.risk_score <= 100:
        return Decision.DENY, "Risk score must be between 0 and 100."

    if request.risk_score >= 80:
        return Decision.DENY, "Risk score is too high."

    if not request.device_managed:
        return Decision.STEP_UP, "Device is unmanaged; verify or remediate device."

    if not request.mfa_verified:
        return Decision.STEP_UP, "Multi-factor authentication has not been verified."

    if request.risk_score >= 50:
        return Decision.STEP_UP, "Medium risk detected; request additional verification."

    return Decision.ALLOW, "Policy checks passed; grant minimum required access."


def demo_requests() -> list[AccessRequest]:
    return [
        AccessRequest("Aarav", "student", "learning-portal", True, True, 12),
        AccessRequest("Meera", "student", "security-console", True, True, 8),
        AccessRequest("Kabir", "staff", "staff-dashboard", False, True, 20),
        AccessRequest("Isha", "staff", "library", True, False, 18),
        AccessRequest("Dev", "admin", "security-console", True, True, 91),
        AccessRequest("Riya", "student", "library", True, True, 57),
    ]


def main() -> None:
    print("=" * 68)
    print("ZTNA EDUCATIONAL ACCESS GATEWAY SIMULATOR")
    print("Project prepared for Shivraj Jarupla")
    print("=" * 68)

    allowed = denied = step_up = 0
    for req in demo_requests():
        decision, reason = evaluate_access(req)
        print(f"\nUser: {req.user} | Role: {req.role} | Resource: {req.resource}")
        print(
            f"Device managed: {req.device_managed} | MFA verified: {req.mfa_verified} "
            f"| Risk: {req.risk_score}/100"
        )
        print(f"Decision: {decision.value}")
        print(f"Reason: {reason}")

        if decision == Decision.ALLOW:
            allowed += 1
        elif decision == Decision.DENY:
            denied += 1
        else:
            step_up += 1

    print("\n" + "-" * 68)
    print("DEMO SUMMARY")
    print(f"Allowed: {allowed} | Denied: {denied} | Additional verification: {step_up}")
    print("Note: This is a simulated policy decision, not a production security gateway.")


if __name__ == "__main__":
    main()
