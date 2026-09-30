'use client';

import {useSearchParams} from 'next/navigation'
import {Suspense} from "react";

function WatchPage() {
  const videoPrefix = 'https://storage.googleapis.com/nc-yt-processed-videos/';
  const videoSrc = useSearchParams().get('v');

  return (
    <div>
      <h1>Watch Page</h1>      
      <video controls src={videoPrefix + videoSrc}/>       
    </div>
  )
}
  
export default function Watch() {
    return (
      // You could have a loading skeleton as the `fallback` too
      <Suspense>
        <WatchPage />
      </Suspense>
    )
}


