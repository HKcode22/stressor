# Deploy Stressor to Netlify

## Quick Setup Instructions

### 1. Install Netlify CLI
```bash
npm install -g netlify-cli
```

### 2. Login to Netlify
```bash
netlify login
```

### 3. Deploy Your Site
```bash
netlify deploy --prod --dir .
```

### 4. Configure Your Site
- Your site will be deployed at: `https://your-site-name.netlify.app`
- The dashboard will be available at: `https://your-site-name.netlify.app/dashboard.html`

## What's Included

- ✅ **Static Landing Page**: Professional homepage
- ✅ **Live Dashboard**: Real-time data with API endpoints
- ✅ **Serverless Functions**: Netlify Functions for API backend
- ✅ **Auto-refresh**: Dashboard updates every 30 seconds
- ✅ **Responsive Design**: Works on all devices

## Features

### Landing Page (`/`)
- Beautiful gradient design
- Feature overview
- Call-to-action buttons

### Live Dashboard (`/dashboard.html`)
- Real-time statistics
- Test run monitoring
- Interactive data visualization
- Auto-refresh functionality

### API Endpoints
- `GET /api/health` - Health check
- `GET /api/stats` - Dashboard statistics
- `GET /api/test-runs` - Recent test runs
- `GET /api/test-runs/{id}/results` - Test results

## Customization

### Update API Data
Edit `netlify/functions/dashboard.py` to modify the data returned by API endpoints.

### Modify Dashboard
Edit `dashboard.html` to change the dashboard appearance and functionality.

### Change Styling
All styles are inline in the HTML files for easy customization.

## Deployment Commands

```bash
# Deploy to staging
netlify deploy

# Deploy to production
netlify deploy --prod

# Deploy with custom directory
netlify deploy --prod --dir .

# Link to existing site
netlify link
```

## Environment Variables

Set these in your Netlify dashboard if needed:
- `PYTHON_VERSION` (default: 3.9)
- Custom API keys or configuration

## Next Steps

1. Deploy to Netlify using the commands above
2. Share your live dashboard URL
3. Customize the design and data as needed
4. Add more API endpoints for additional functionality
