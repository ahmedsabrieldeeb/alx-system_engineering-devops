# Postmortem Review

## Issue Summary

- **Outage Duration:** The issue occurred from 08:30 AM to 08:45 AM (UTC) during the initial ApacheBench test, causing a surge in failed requests.
- **Impact:** A significant percentage of requests (943 out of 2000) failed within the specified timeframe, impacting server performance.
- **Root Cause:** The Nginx default file limit (15) led to connection issues during high concurrency.

## Timeline

- **Detection:** Uncovered at 08:30 AM (UTC) through NewRelic monitoring, which highlighted a sudden increase in failed requests.
- **Actions:** Utilized NewRelic insights, focusing on ApacheBench results, and identified the low Nginx file limit as the root cause by 08:35 AM (UTC).
- **Escalation:** PagerDuty alerted the on-call team at 08:35 AM (UTC) based on the severity detected by NewRelic.
- **Resolution:** Successfully increased the file limit to 4096 in the Nginx configuration, followed by a server restart by 08:45 AM (UTC).

## Root Cause and Resolution

- **Root Cause:** Nginx default file limit set too low (15), causing connection problems.
- **Resolution:** Raised file limit to 4096 in Nginx config and restarted the server.

## Corrective and Preventative Measures

- **Fixes:**
  - Updated Nginx config for a higher default file limit.
- **Tasks:**
  - Adjusted Nginx config for a file limit of 4096.
  - Incorporated regular server config reviews to ensure optimal performance.
- **Monitoring and On-Call:**
  - Enhanced reliance on NewRelic for proactive issue detection.
  - Leveraged PagerDuty for efficient on-call team notification and incident management.
