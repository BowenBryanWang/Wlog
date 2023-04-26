import React, { ReactNode } from 'react';

interface Props {
  content: any;
}

const FormatHtml: React.FC<Props> = ({ content }) => (
  <div
    dangerouslySetInnerHTML={{
      __html: content
    }}
  />
);

export default FormatHtml;
