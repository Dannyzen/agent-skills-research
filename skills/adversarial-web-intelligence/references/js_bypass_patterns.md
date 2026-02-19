# JS Bypass & Headless Browser Patterns

Use these patterns when a site returns a blank body or "Enable JavaScript" message.

## Puppeteer Initialization (Node.js)

```javascript
const browser = await puppeteer.launch({
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
  headless: 'new'
});
const page = await browser.newPage();

// Emulate a standard desktop agent to avoid bot-detection
await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36...');
```

## Effective SPA Navigation
```javascript
// Wait for specific UI elements that indicate full render
await page.goto(url, { waitUntil: 'networkidle2' });
await page.waitForSelector('#comment-section', { timeout: 15000 });

// Extract clean text for LLM ingestion
const cleanContent = await page.evaluate(() => {
  return document.querySelector('article').innerText;
});
```

## Dependency Requirements (Linux)
Ensure the following system libraries are present:
`libatk-1.0-0`, `libnss3`, `libcups2`, `libxcomposite1`, `libxdamage1`, `libxrandr2`.
