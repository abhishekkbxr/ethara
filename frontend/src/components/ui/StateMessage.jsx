export default function StateMessage({ type = 'neutral', message }) {
  return <div className={`state-message state-message--${type}`}>{message}</div>;
}
