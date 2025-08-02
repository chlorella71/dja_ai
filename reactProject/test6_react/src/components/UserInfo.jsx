import React, {memo} from 'react';

const UserInfo = memo(({user}) => {
  return (
    <div>
        <h2>UserInfo</h2>
      {user.name} ({user.age})
    </div>
  );
})

export default UserInfo;
