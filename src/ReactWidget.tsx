import React from 'react';
import { WidgetModel } from '@jupyter-widgets/base';
import { WidgetModelContext } from './hooks/widget-model';

import CanopyChart from './CanopyChart';

interface WidgetProps {
  model: WidgetModel;
}

function ReactWidget(props: WidgetProps) {
  return <CanopyChart />;
}

function withModelContext(Component: (props: WidgetProps) => JSX.Element) {
  return (props: WidgetProps) => (
    <WidgetModelContext.Provider value={props.model}>
      <Component {...props} />
    </WidgetModelContext.Provider>
  );
}

export default withModelContext(ReactWidget);
