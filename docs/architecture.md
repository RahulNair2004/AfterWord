                                          AFTERWORDS
                                              │
                                     ┌────────┴────────┐
                                     │                 │
                                 React +           Tailwind
                                 Router             CSS
                                     │
                                     ▼
                                REST API
                                     │
                                     ▼
                              ┌──────────────┐
                              │   FastAPI    │
                              │ Modular      │
                              │ Monolith     │
                              └──────┬───────┘
                                     │
                   ┌─────────────────┼────────────────────┐
                   │                 │                    │
                   ▼                 ▼                    ▼
               Core Modules      Investigation           AI
                   │                 │                    │
                   │        ┌────────┼────────┐           │
                   │        ▼        ▼        ▼           │
                   │      Cases   Evidence  Theories      │
                   │        │        │        │           │
                   │        └────────┼────────┘           │
                   │                 ▼                    │
                   │          Investigations              │
                   │                 │                    │
                   ├──────────► Social ◄──────────────────┤
                   │                 │
                   ├──────────► Search
                   │
                   ├──────────► Recommendations
                   │
                   ├──────────► Notifications
                   │
                   └──────────► Moderation
                                     │
                                     ▼
                          ┌─────────────────────┐
                          │      PostgreSQL     │
                          │   Source of Truth   │
                          └──────────┬──────────┘
                                     │
                                     │
                              ┌──────▼──────┐
                              │  Amazon S3  │
                              │    Media    │
                              └─────────────┘