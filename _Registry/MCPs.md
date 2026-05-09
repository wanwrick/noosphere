# MCP Connectors Registry

> Connected services available via Model Context Protocol. These provide live data access, not embedded in this project but referenced for routing.

---

## Active Connectors

| Service | Capabilities | When to Use |
|---------|-------------|-------------|
| **Notion** | Search, read pages, create pages, update pages, query databases, manage comments | Live reference for engagement context, meeting notes, sprint data — **always fetch by page ID** (see CLAUDE.md Reference Map) |
| **GitHub** | List/read/create PRs, issues, files, branches, releases; CI status; review comments | Practice repo PR review, branch management, sanitization workflow runs |
| **Diagram (mermaid / svg / markdown)** | Generate Mermaid diagrams, draw SVG, create markdown documents | Architecture diagrams in `_Diagrams/` and `methodology/diagram-generation.md` |
| **Gmail** | Search messages, read threads, create drafts, get profile | Email drafts, searching correspondence, stakeholder communication |
| **Google Calendar** | List events, create events, find meeting times, check free time | Scheduling, meeting prep, availability checks |
| **Google Drive** | Search files, read documents | Finding docs, reading shared documents |
| **Canva** | Search designs, create designs, edit designs, export | Visual content, presentations, social media |
| **Figma** | Get design context, screenshots, metadata, variables | UI/UX review, design-to-code, component mapping |

---

## Usage Patterns

### Notion (Primary Knowledge Base)
```
Search → notion-search (semantic search across workspace)
Read → notion-fetch (get page content by URL or ID)
Create → notion-create-pages (new pages with markdown content)
Update → notion-update-page (modify properties or content)
Query → notion-query-database-view (query database views)
```

### Gmail (Communication)
```
Find emails → gmail_search_messages (Gmail search syntax)
Read → gmail_read_message or gmail_read_thread
Draft → gmail_create_draft (never sends without confirmation)
```

### Google Calendar (Scheduling)
```
View schedule → gcal_list_events (time range + calendar)
Find availability → gcal_find_meeting_times (multi-person)
My free time → gcal_find_my_free_time
Create event → gcal_create_event (with attendees, meet link)
```

### Google Drive (Document Access)
```
Search → google_drive_search (query syntax)
Read → google_drive_fetch (by document ID)
```

---

## Important Notes

- **Notion is the live reference**: meeting notes, project docs, and team wikis live there
- **Gmail drafts only**: Claude creates drafts, never sends without explicit approval
- **Calendar actions**: creating events requires confirmation
- **All MCPs require active connection**: if a connector isn't available, fall back to the knowledge in this project
- **GitHub MCP scope (v1.2.0)**: tools are restricted to `wanwrick/noosphere`. Never read from or write to other repositories.
- **Diagram MCP usage (v1.2.0)**: produce Mermaid first; reserve SVG for final whiteboard renders. All diagrams follow the palette + layout rules in `methodology/diagram-generation.md`. Do not commit `.excalidraw` files.

---

*Last updated: 2026-05-09 (v1.2.0 — added GitHub + Diagram MCPs; clarified Notion as live reference)*
