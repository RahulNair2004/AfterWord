                    USER
                     │
                     ▼
              React Login/Register
                     │
                     ▼
                FastAPI Auth
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
     Validate Input       Verify Password
                                │
                                ▼
                           PostgreSQL
                                │
                                ▼
                         Create Session/
                            Token
                                │
                                ▼
                         React Client
                                │
                                ▼
                     Authenticated Requests
                                │
                                ▼
                       Auth Dependency
                                │
                                ▼
                         Current Use

## Authorization ##         
                            
                            Request
                            
                              ↓
                            
                            Authenticated?
                            
                              ↓
                            
                            User Role
                            
                              ↓
                            
                            Resource Ownership
                            
                              ↓
                            
                            Permission
                            
                              ↓
                            

                            Allow / Deny