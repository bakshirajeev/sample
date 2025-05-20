import React, { useEffect, useState } from 'react';

function App() {
  const [catalog, setCatalog] = useState(null);

  useEffect(() => {
    fetch('/api/catalog')
      .then((r) => r.json())
      .then(setCatalog)
      .catch(console.error);
  }, []);

  if (!catalog) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Power BI Catalog</h1>
      <pre>{JSON.stringify(catalog, null, 2)}</pre>
    </div>
  );
}

export default App;
