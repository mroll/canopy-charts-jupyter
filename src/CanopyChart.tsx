import React from 'react';
import { useModelState } from './hooks/widget-model';
import { CanopyChart } from 'canopy-charts';

export default function JupyterCanopyChart() {
  const [id] = useModelState('id');
  const [table] = useModelState('table');

  return (
    <div style={{ height: 400 }}>
      <CanopyChart id={id} table={table} height={300} />
    </div>
  );
}
