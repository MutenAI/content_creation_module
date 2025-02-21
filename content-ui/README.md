# Content Creation UI

Interfaccia utente moderna per il sistema di creazione contenuti basato su AI. Questa applicazione fornisce un'interfaccia intuitiva per interagire con il nostro sistema multi-agente di generazione contenuti.

## 🚀 Tecnologie

- **Next.js 15** - Framework React per la produzione
- **TypeScript** - Tipizzazione statica per JavaScript
- **Tailwind CSS** - Framework CSS utility-first
- **@tailwindcss/forms** - Plugin Tailwind per styling dei form

## 📁 Struttura del Progetto

```
content-ui/
├── pages/           # Route pages
├── components/      # Componenti React riutilizzabili
├── styles/         # File CSS e configurazioni Tailwind
├── public/         # Asset statici
└── types/          # Definizioni TypeScript
```

## 🛠️ Setup & Installazione

1. **Clona il repository e installa le dipendenze**
   ```bash
   git clone <repository-url>
   cd content-ui
   npm install
   ```

2. **Avvia il server di sviluppo**
   ```bash
   npm run dev
   ```
   L'applicazione sarà disponibile su [http://localhost:3000](http://localhost:3000)

## 🔧 Configurazione

- `tailwind.config.js` - Configurazione Tailwind CSS
- `styles/globals.css` - Stili globali e direttive Tailwind
- `tsconfig.json` - Configurazione TypeScript

## 📦 Dipendenze Principali

- `next`: ^15.1.7
- `react`: ^18
- `react-dom`: ^18
- `typescript`: ^5
- `tailwindcss`: ^3
- `@tailwindcss/forms`: ^0.5

## 🤝 Contribuire

1. Fai il fork del progetto
2. Crea il tuo branch (`git checkout -b feature/AmazingFeature`)
3. Committa i tuoi cambiamenti (`git commit -m 'Add some AmazingFeature'`)
4. Pusha sul branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📝 Note

- Assicurati di avere Node.js 18+ installato
- Usa `npm run build` per la build di produzione
- Controlla `package.json` per altri script disponibili

## 📄 Licenza

Distribuito sotto licenza MIT. Vedi `LICENSE` per maggiori informazioni.

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `pages/index.tsx`. The page auto-updates as you edit the file.

[API routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) can be accessed on [http://localhost:3000/api/hello](http://localhost:3000/api/hello). This endpoint can be edited in `pages/api/hello.ts`.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) instead of React pages.

This project uses [`next/font`](https://nextjs.org/docs/pages/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn-pages-router) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/pages/building-your-application/deploying) for more details.
