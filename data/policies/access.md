# ACCESS-001 - Access policy (fictional Contoso Manufacturing)

Version 1, effective for this synthetic exercise only.

- Only users `user-01`, `user-02`, `user-03` exist in the lab directory.
- Phoenix owner: `owner-phoenix`; members: user-01 and user-02.
- Atlas owner: `owner-atlas`; member: user-03.
- user-01 already has Reader access to Phoenix. Repeated requests are Resolve.
- A project member's Reader request is pre-authorized: Execute the mock request.
- Contributor access and non-member Reader access require the project owner's
  approval: Route. A queued request does not grant permission.
- Owner access requires a security review: Escalate, never grant automatically.
- Missing project or role: Route to request the missing information. Do not guess.
- Unknown users, unknown projects and unsupported roles are explicit tool errors.
- Reusing a request ID with changed arguments is an error.

All operations are simulations. Never change real Azure permissions.
